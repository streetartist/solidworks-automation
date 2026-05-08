# IGetStereoSeparation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetStereoSeparation`

Obsolete and not superseded. Functionality no longer implemented.
Obsolete and not superseded. Functionality no longer implemented.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetStereoSeparation() As System.Double
```

```

Dim instance As IModelView
Dim value As System.Double
 
value = instance.IGetStereoSeparation()
```

```

System.double IGetStereoSeparation()
```

```

System.double IGetStereoSeparation(); 
```

#### Return Value

Array of 2 doubles representing the stereo magnitude and stereo parallax balance settings

Remarks

This method checks the two stereoscopic display values which can be set by using [IModelView::SetStereoSeparation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetStereoSeparation.md) or [IModelView::ISetStereoSeparation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetStereoSeparation.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
