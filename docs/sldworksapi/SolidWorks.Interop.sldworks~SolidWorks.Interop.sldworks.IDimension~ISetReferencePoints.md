# ISetReferencePoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetReferencePoints`

Sets the reference points for this dimension.
Sets the reference points for this dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetReferencePoints( _
   ByVal PointsCount As System.Integer, _
   ByRef RefPoints As MathPoint _
) 
```

```

Dim instance As IDimension
Dim PointsCount As System.Integer
Dim RefPoints As MathPoint
 
instance.ISetReferencePoints(PointsCount, RefPoints)
```

```

void ISetReferencePoints( 
   System.int PointsCount,
   ref MathPoint RefPoints
)
```

```

void ISetReferencePoints( 
   System.int PointsCount,
   MathPoint^% RefPoints
) 
```

#### Parameters

*PointsCount*
:   Number of reference points for this dimension

*RefPoints*
:   Pointer to the [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::IGetReferencePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetReferencePoints.md)  
[IDimension::ReferencePoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReferencePoints.md)  
[IDimension::GetReferencePointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetReferencePointsCount.md)
