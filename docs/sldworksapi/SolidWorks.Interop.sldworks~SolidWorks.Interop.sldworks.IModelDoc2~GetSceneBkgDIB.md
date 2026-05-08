# GetSceneBkgDIB Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneBkgDIB`

Gets background image as a LPDIBSECTION.
Gets background image as a LPDIBSECTION.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSceneBkgDIB() As System.Integer
```

```

Dim instance As IModelDoc2
Dim value As System.Integer
 
value = instance.GetSceneBkgDIB()
```

```

System.int GetSceneBkgDIB()
```

```

System.int GetSceneBkgDIB(); 
```

#### Return Value

Background image as DIBSECTION

Remarks

If your application must be x64 compatible, then use [IModelDocExtension::GetSceneBkgDIBx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSceneBkgDIBx64.md).

The memory for the image bits (DIBSECTION.dsBm.bmBits) and this structure are allocated by the SOLIDWORKS application and must be deleted by the caller.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSceneBkgDIB.md)  
[IModelDocExtension::SetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSceneBkgDIBx64.md)  
[IModelDoc2::SceneBkgImageFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneBkgImageFileName.md)  
[IModelDoc2::InsertBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.md)  
[IModelDoc2::DeleteBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteBkgImage.md)
