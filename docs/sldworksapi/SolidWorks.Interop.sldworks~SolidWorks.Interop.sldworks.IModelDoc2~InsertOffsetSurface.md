# InsertOffsetSurface Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertOffsetSurface`

Inserts an offset surface.
Inserts an offset surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertOffsetSurface( _
   ByVal Thickness As System.Double, _
   ByVal Reverse As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Thickness As System.Double
Dim Reverse As System.Boolean
 
instance.InsertOffsetSurface(Thickness, Reverse)
```

```

void InsertOffsetSurface( 
   System.double Thickness,
   System.bool Reverse
)
```

```

void InsertOffsetSurface( 
   System.double Thickness,
   System.bool Reverse
) 
```

#### Parameters

*Thickness*
:   Offset of surface from reference

*Reverse*
:   True to reverse the direction of the offset, false to not

Remarks

Make the selections using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) before calling this method.

See the SOLIDWORKS Help for more information about what entities are valid for selection.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.md)  
[IBody2::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateOffsetSurface.md)  
[IBody2::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateOffsetSurface.md)  
[IBody2::MakeOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MakeOffset.md)  
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.md)  
[IModeler::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateOffsetSurface.md)  
[ISurface::GetOffsetSurfParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetOffsetSurfParams2.md)  
[ISurface::IGetOffsetSurfParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetOffsetSurfParams2.md)  
[ISurface::IsOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsOffset.md)
