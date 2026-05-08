# SetSceneBkgDIBx64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSceneBkgDIBx64`

Sets the background image in 64-bit applications.
Sets the background image in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSceneBkgDIBx64( _
   ByVal L_dib As System.Long _
) 
```

```

Dim instance As IModelDocExtension
Dim L_dib As System.Long
 
instance.SetSceneBkgDIBx64(L_dib)
```

```

void SetSceneBkgDIBx64( 
   System.long L_dib
)
```

```

void SetSceneBkgDIBx64( 
   System.int64 L_dib
) 
```

#### Parameters

*L\_dib*
:   Background image as DIBSECTION

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Old background images are deleted automatically.

 

For more information about DIBSECTION, see MicroSoft's documentation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSceneBkgDIBx64.md)  
[IModelDoc2::GetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneBkgDIB.md)  
[IModelDoc2::SetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSceneBkgDIB.md)  
[IModelDoc2::InsertBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.md)  
[IModelDoc2::SceneBkgImageFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneBkgImageFileName.md)
