# GetSceneBkgDIBx64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSceneBkgDIBx64`

Gets the background image as DIBSECTION in 64-bit applications.
Gets the background image as DIBSECTION in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSceneBkgDIBx64() As System.Long
```

```

Dim instance As IModelDocExtension
Dim value As System.Long
 
value = instance.GetSceneBkgDIBx64()
```

```

System.long GetSceneBkgDIBx64()
```

```

System.int64 GetSceneBkgDIBx64(); 
```

#### Return Value

Background image as DIBSECTION

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

The memory for the image bits ( DIBSECTION.dsBm.bmBits) and this structure are allocated by the SOLIDWORKS application and must be deleted by the caller.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::SetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSceneBkgDIBx64.md)  
[IModelDoc2::GetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneBkgDIB.md)  
[IModelDoc2::SetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSceneBkgDIB.md)  
[IModelDoc2::InsertBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.md)  
[IModelDoc2::SceneBkgImageFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneBkgImageFileName.md)
