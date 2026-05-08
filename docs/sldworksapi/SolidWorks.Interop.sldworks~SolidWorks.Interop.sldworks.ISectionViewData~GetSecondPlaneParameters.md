# GetSecondPlaneParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetSecondPlaneParameters`

Gets the second transformed plane's parameters for this section view.
Gets the second transformed plane's parameters for this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetSecondPlaneParameters( _
   ByRef PlaneCenter As MathPoint, _
   ByRef PlaneVector As MathVector _
) 
```

```

Dim instance As ISectionViewData
Dim PlaneCenter As MathPoint
Dim PlaneVector As MathVector
 
instance.GetSecondPlaneParameters(PlaneCenter, PlaneVector)
```

```

void GetSecondPlaneParameters( 
   out MathPoint PlaneCenter,
   out MathVector PlaneVector
)
```

```

void GetSecondPlaneParameters( 
   [Out] MathPoint^ PlaneCenter,
   [Out] MathVector^ PlaneVector
) 
```

#### Parameters

*PlaneCenter*
:   [Plane center point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

*PlaneVector*
:   [Plane normal vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)  
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.md)  
[ISectionViewData::GetFirstPlaneParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetFirstPlaneParameters.md)  
[ISectionViewData::GetThirdPlaneParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetThirdPlaneParameters.md)  
[ISectionViewData::FirstPlane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstPlane.md)  
[ISectionViewData::SecondPlane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondPlane.md)  
[ISectionViewData::ThirdPlane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdPlane.md)
