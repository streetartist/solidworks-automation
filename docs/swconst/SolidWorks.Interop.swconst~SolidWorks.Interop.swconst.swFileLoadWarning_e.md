# swFileLoadWarning_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e`

File load warnings for ISldWorks::OpenDoc6. Bitmask.
File load warnings for [ISldWorks::OpenDoc6](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html). [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("881A610B-F5A0-4969-90F3-FF2A1DEF6921")>
Public Enum swFileLoadWarning_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFileLoadWarning_e
```

```

[System.Runtime.InteropServices.Guid("881A610B-F5A0-4969-90F3-FF2A1DEF6921")]
public enum swFileLoadWarning_e : System.Enum 
```

```

public enum swFileLoadWarning_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("881A610B-F5A0-4969-90F3-FF2A1DEF6921")
public enum swFileLoadWarning_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("881A610B-F5A0-4969-90F3-FF2A1DEF6921")]
__value public enum swFileLoadWarning_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("881A610B-F5A0-4969-90F3-FF2A1DEF6921")]
public enum class swFileLoadWarning_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFileLoadWarning\_AlreadyOpen** | 128 or 0x80 = Warning appears because the document is already open. |
| **swFileLoadWarning\_AutomaticRepair** | 262144 or 0x40000 = Warning appears that non-critical data in the document was automatically repaired. |
| **swFileLoadWarning\_BasePartNotLoaded** | 64 or 0x40 = Warning appears because the document was defined in the context of another existing document that is not loaded. |
| **swFileLoadWarning\_ComponentMissingReferencedConfig** | 32768 or 0x8000 = Warning appears if document is opened silently and swOpenDocOptions\_AutoMissingConfig is specified. |
| **swFileLoadWarning\_CriticalDataRepair** | 524288 or 0x80000 = Warning appears that critical data in the document was automatically repaired. |
| **swFileLoadWarning\_DimensionsReferencedIncorrectlyToModels** | 16384 or 0x4000 = Warning appears because some dimensions are referenced to the models incorrectly; these dimensions are highlighted in red in the drawing. |
| **swFileLoadWarning\_DrawingANSIUpdate** | 8 or 0x8 = Warning appears because radial dimension arrows now displayed outside when the dimension text is outside of the arc or circle. |
| **swFileLoadWarning\_DrawingSFSymbolConvert** | 2048 or 0x800Warning appears asking the user if he or she wants to convert this drawing's surface finish symbols to the sizes specified in ANSI Y14.36M-1996 and ISO 1302-1978. |
| **swFileLoadWarning\_DrawingsOnlyRapidDraft** | 256 or 0x100 = Warning appears because the only RapidDraft format conversion that can take place is a drawing document that is not Detached. |
| **swFileLoadWarning\_IdMismatch** | 1 or 0x1 = Warning appears if the internal ID of the document does not match the internal ID saved with the referencing document. |
| **swFileLoadWarning\_InvisibleDoc\_LinkedDesignTableUpdateFail** | 65536 or 0x10000 = Warning issued because an attempt has been made to open an invisible document with a linked design table that was modified externally, and the design table cannot be updated because the document cannot be displayed; you must make the document visible to open it and update the design table. |
| **swFileLoadWarning\_MissingDesignTable** | 131072 or 0x20000 = Warning appears because the design table is missing. |
| **swFileLoadWarning\_MissingExternalReferences** | 1048576 or 0x100000 = Warning appears if one or more references are missing when loading a file. |
| **swFileLoadWarning\_ModelOutOfDate** | 8192 or 0x2000 = Warning appears because some sheets contain drawing views that are out of date with their external models. |
| **swFileLoadWarning\_NeedsRegen** | 32 or 0x20 = Warning appears because the document needs to be rebuilt. |
| **swFileLoadWarning\_ReadOnly** | 2 or 0x2 = Warning appears because the document is read only. |
| **swFileLoadWarning\_RevolveDimTolerance** | 4096 or 0x1000 = Warning appears because some of the tolerances of the revolved feature dimensions were created in SOLIDWORKS 99 or earlier and are not synchronized with their corresponding dimensions in the sketch. |
| **swFileLoadWarning\_SharingViolation** | 4 or 0x4 = Warning appears if the document is being used by another user. |
| **swFileLoadWarning\_SheetScaleUpdate** | 16 or 0x10 = Warning appears because SOLIDWORKS now applies the scale of the sheet to the sketch entities on the sheet; which means that the sheet looks the same but dimension values are scaled. |
| **swFileLoadWarning\_ViewMissingReferencedConfig** | 1024 or 0x400 = Warning appears because a configuration that a drawing view is referencing no longer exists in the model (part or assembly); the active configuration is used. |
| **swFileLoadWarning\_ViewOnlyRestrictions** | 512 or 0x200 = Warning appears because the document is view only and a configuration other than the default configuration is set. |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFileLoadWarning\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
