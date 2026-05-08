# SetSceneBkgDIB Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSceneBkgDIB`

Sets background image described by DIBSECTION data.
Sets background image described by DIBSECTION data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSceneBkgDIB( _
   ByVal L_dib As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim L_dib As System.Integer
 
instance.SetSceneBkgDIB(L_dib)
```

```

void SetSceneBkgDIB( 
   System.int L_dib
)
```

```

void SetSceneBkgDIB( 
   System.int L_dib
) 
```

#### Parameters

*L\_dib*
:   DIBSECTION

Remarks

If your application must be x64 compatible, then use [IModelDocExtension::SetSceneBkgDIBx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSceneBkgDIBx64.md).

Old background images are deleted automatically.

For more information about DIBSECTION, see Microsoft's documentation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneBkgDIB.md)  
[IModelDocExtension::GetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSceneBkgDIBx64.md)  
[IModelDocExtension::InsertBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.md)  
[IModelDocExtension::DeleteBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteBkgImage.md)  
[IModelDocExtension::SceneBkgImageFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneBkgImageFileName.md)
