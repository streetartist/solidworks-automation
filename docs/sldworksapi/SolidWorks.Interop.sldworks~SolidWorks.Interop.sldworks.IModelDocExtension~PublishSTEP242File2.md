# PublishSTEP242File2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishSTEP242File2`

Exports the SOLIDWORKS MBD 3D part or assembly to a STEP 242 file.
Exports the SOLIDWORKS MBD 3D part or assembly to a STEP 242 file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PublishSTEP242File2( _
   ByVal MBDSTEP242Data As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim MBDSTEP242Data As System.Object
Dim value As System.Integer
 
value = instance.PublishSTEP242File2(MBDSTEP242Data)
```

```

System.int PublishSTEP242File2( 
   System.object MBDSTEP242Data
)
```

```

System.int PublishSTEP242File2( 
   System.Object^ MBDSTEP242Data
) 
```

#### Parameters

*MBDSTEP242Data*
:   [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.md)

#### Return Value

Status as defined in [swStep242Error\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStep242Error_e.html)

Remarks

This method requires that the SOLDWORKS MBD add-in be loaded. ([ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.md))

See the SOLIDWORKS Help for details about MBD.

Example

See the IMBDSTEP242Data example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::PublishTo3DPDF Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.md)  
[IMBD3DPdfData::CreateAttachSTEP242 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CreateAttachSTEP242.md)
