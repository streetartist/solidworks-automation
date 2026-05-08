# swSaveAsOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveAsOptions_e`

Save As options. Bitmask.
Save As options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("A39D1A60-DD4A-4118-8227-4FA71CCCDD80")>
Public Enum swSaveAsOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSaveAsOptions_e
```

```

[System.Runtime.InteropServices.Guid("A39D1A60-DD4A-4118-8227-4FA71CCCDD80")]
public enum swSaveAsOptions_e : System.Enum 
```

```

public enum swSaveAsOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("A39D1A60-DD4A-4118-8227-4FA71CCCDD80")
public enum swSaveAsOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("A39D1A60-DD4A-4118-8227-4FA71CCCDD80")]
__value public enum swSaveAsOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("A39D1A60-DD4A-4118-8227-4FA71CCCDD80")]
public enum class swSaveAsOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSaveAsOptions\_AvoidRebuildOnSave** | 8 or 0x8 |
| **swSaveAsOptions\_Copy** | 2 or 0x2; Save the document as a copy and continue editing |
| **swSaveAsOptions\_CopyAndOpen** | 512 or 0x200; Save the document as a copy and open it |
| **swSaveAsOptions\_DetachedDrawing** | Obsolete. |
| **swSaveAsOptions\_ExportTo2DPdfFromInspection** | 2048 or 0x800; Export drawing sheets from Inspection to 2DPdf |
| **swSaveAsOptions\_IgnoreBiography** | 256 or 0x100; Prune a SOLIDWORKS file's revision history to just the current file name |
| **swSaveAsOptions\_IncludeVirtualSubAsmComps** | 1024 or 0x400; Save regular components in virtual subassemblies |
| **swSaveAsOptions\_OverrideSaveEmodel** | 32 or 0x20; Saves eDrawings-related information into a section of the file being saved; specifying this setting overrides the Tools, Options, System Options, General, Save eDrawings data in SOLIDWORKS document setting; not a valid option for [IPartDoc::SaveToFile2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~SaveToFile2.html) |
| **swSaveAsOptions\_SaveEmodelData** | Obsolete. |
| **swSaveAsOptions\_SaveReferenced** | 4 or 0x4; Supports parts, assemblies, and drawings; this setting indicates to save all components (sub-assemblies and parts) in both assemblies and drawings; if a part has an external reference, then this setting indicates to save the external reference |
| **swSaveAsOptions\_Silent** | 1 or 0x1 |
| **swSaveAsOptions\_UpdateInactiveViews** | 16 or 0x10; Not a valid option for [IPartDoc::SaveToFile2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~SaveToFile2.html); this setting is only applicable for a drawing that has one or more sheets; this setting updates the views on inactive sheets |

Remarks

These options only apply to saving to native SOLIDWORKS file formats. For example, to export a SOLIDWORKS file to a VRML file format, use [ISldWorks::GetUserPreferenceToggle](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html) and [ISldWorks::SetUserPreferenceToggle](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) with swExportVrmlAllComponentsInSingleFile.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSaveAsOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
