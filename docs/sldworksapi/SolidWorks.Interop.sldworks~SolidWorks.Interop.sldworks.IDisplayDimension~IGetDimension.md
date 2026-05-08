# IGetDimension Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IGetDimension`

Obsolete. Superseded by IDisplayDimension::GetDimension2.
Obsolete. Superseded by [IDisplayDimension::GetDimension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetDimension2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDimension() As Dimension
```

```

Dim instance As IDisplayDimension
Dim value As Dimension
 
value = instance.IGetDimension()
```

```

Dimension IGetDimension()
```

```

Dimension^ IGetDimension(); 
```

#### Return Value

Pointer to an [IDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md) object

Remarks

SOLIDWORKS can display a dimension more than once. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) object in the SOLIDWORKS API. The original base-extrude dimension is represented by the [IDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md) object in the SOLIDWORKS API.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetDimension.md)  
[IFeature::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IParameter.md)  
[IFeature::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Parameter.md)  
[IModelDoc2::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IParameter.md)  
[IModelDoc2::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Parameter.md)
