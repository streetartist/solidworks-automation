# swPropertyManagerPageOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertyManagerPageOptions_e`

Options for PropertyManager pages. Bitmask.
Options for PropertyManager pages. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("92BC2AEE-0E3A-40EF-923D-EFD935545505")>
Public Enum swPropertyManagerPageOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPropertyManagerPageOptions_e
```

```

[System.Runtime.InteropServices.Guid("92BC2AEE-0E3A-40EF-923D-EFD935545505")]
public enum swPropertyManagerPageOptions_e : System.Enum 
```

```

public enum swPropertyManagerPageOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("92BC2AEE-0E3A-40EF-923D-EFD935545505")
public enum swPropertyManagerPageOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("92BC2AEE-0E3A-40EF-923D-EFD935545505")]
__value public enum swPropertyManagerPageOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("92BC2AEE-0E3A-40EF-923D-EFD935545505")]
public enum class swPropertyManagerPageOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPropertyManagerOptions\_AbortCommands** | 1024 or 0x400; Abort active command when PropertyManager page is displayed |
| **swPropertyManagerOptions\_AllowHorizontalResize** | Obsolete; as of SOLIDWORKS 2006 and later, all PropertyManager pages can be resized horizontally |
| **swPropertyManagerOptions\_CancelButton** | 2 or 0x2 |
| **swPropertyManagerOptions\_CanEscapeCancel** | 4096 or 0x1000; When a user presses the Esc key, the PropertyManager page will close the page; this enumerator only applies to pages that do not contain selection boxes |
| **swPropertyManagerOptions\_CloseDialogButton** | 8 or 0x8 |
| **swPropertyManagerOptions\_DisablePageBuildDuringHandlers** | 32768 or 0x8000; Paint the PropertyManager page after control returns to SOLIDWORKS from the add-in's handler; may help eliminate any flickering of the PropertyManager page of the add-in changes the visibility of numerous controls on the PropertyManager page |
| **swPropertyManagerOptions\_DisableSelection** | 256 or 0x100 |
| **swPropertyManagerOptions\_GrayOutDisabledSelectionListboxes** | 65536 or 0x10000; Controls whether a PropertyManager page should show its disabled selection list boxes so that they appear grayed out by coloring their backgrounds the same color as the divider box background.     **NOTE:** Disabled selection list boxes should be hidden; graying them out is an exception to SOLIDWORKS standard practice. |
| **swPropertyManagerOptions\_HandleKeystrokes** | 8192 or 0x2000; Enables processing of keystrokes while the PropertyManager page is displayed; disabled by default |
| **swPropertyManagerOptions\_LockedPage** | 4 or 0x4 |
| **swPropertyManagerOptions\_MultiplePages** | 16 or 0x10 |
| **swPropertyManagerOptions\_OkayButton** | 1 or 0x1 |
| **swPropertyManagerOptions\_PreviewButton** | 128 or 0x80 |
| **swPropertyManagerOptions\_PushpinButton** | 32 or 0x20 |
| **swPropertyManagerOptions\_RedoButton** | 16384 or 0x4000; |
| **swPropertyManagerOptions\_SupportsChainSelection** | 131072 or 0x20000; If set, then show **Select Chain**:   - on the shortcut menu if a sketch entity is currently selected.    - or - - if nothing is selected, but the cursor is over a sketch entity when the right-mouse button was clicked. |
| **swPropertyManagerOptions\_SupportsIsolate** | 262144 or 0x40000; If set, then show **Isolate** item in right-mouse button menu of assembly components. This option must be used with swPropertyManagerOptions\_LockedPage. |
| **swPropertyManagerOptions\_UndoButton** | 2048 or 0x800 |
| **swPropertyManagerOptions\_WhatsNew** | 512 or 0x200; Indicates that you want a What's New button to appear on your PropertyManager page |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPropertyManagerPageOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
