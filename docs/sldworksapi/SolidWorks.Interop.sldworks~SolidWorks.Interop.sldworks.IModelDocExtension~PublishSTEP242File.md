# PublishSTEP242File Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishSTEP242File`

Obsolete. Superseded by IModelDocExtension::PublishSTEP242File2.
Obsolete. Superseded by [IModelDocExtension::PublishSTEP242File2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishSTEP242File2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PublishSTEP242File( _
   ByVal Path As System.String _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim Path As System.String
Dim value As System.Integer
 
value = instance.PublishSTEP242File(Path)
```

```

System.int PublishSTEP242File( 
   System.string Path
)
```

```

System.int PublishSTEP242File( 
   System.String^ Path
) 
```

#### Parameters

*Path*
:   Full qualified path to which to export the SOLIDWORKS MBD 3D part or assembly; use **.STP** for the file name extension

#### Return Value

Status as defined in [swStep242Error\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStep242Error_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::PublishTo3DPDF Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.md)  
[IMBD3DPdfData::CreateAttachSTEP242 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CreateAttachSTEP242.md)
