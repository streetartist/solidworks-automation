# GetDirectionReference Method (ISimpleHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetDirectionReference`

Gets the direction of the cut extrude for this simple hole feature.
Gets the direction of the cut extrude for this simple hole feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDirectionReference( _
   ByRef Ref1 As System.Object, _
   ByRef Type1 As System.Integer, _
   ByRef Ref2 As System.Object, _
   ByRef Type2 As System.Integer _
) As System.Integer
```

```

Dim instance As ISimpleHoleFeatureData2
Dim Ref1 As System.Object
Dim Type1 As System.Integer
Dim Ref2 As System.Object
Dim Type2 As System.Integer
Dim value As System.Integer
 
value = instance.GetDirectionReference(Ref1, Type1, Ref2, Type2)
```

```

System.int GetDirectionReference( 
   out System.object Ref1,
   out System.int Type1,
   out System.object Ref2,
   out System.int Type2
)
```

```

System.int GetDirectionReference( 
   [Out] System.Object^ Ref1,
   [Out] System.int Type1,
   [Out] System.Object^ Ref2,
   [Out] System.int Type2
) 
```

#### Parameters

*Ref1*
:   First reference entity (see **Remarks**)

*Type1*
:   Type of reference entity as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

*Ref2*
:   Second reference entity (see Remarks)

*Type2*
:   Type of reference entity as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

Number of reference entities used to define the direction of this hole feature

Remarks

Sometimes one reference entity defines a direction; for example, an edge or axis. Other times, two reference entities define a direction; for example, two vertices or two sketch points.

|  |  |
| --- | --- |
| **If...** | **Then...** |
| One reference entity defined the direction | Ref2 is NULL and the return value  is 1 |
| Two reference entities defined the direction | Both Ref1 and Ref2 are non-NULL and return value is 2 |

Valid reference entities for Ref1 and Ref2:

- line segment
- edge
- axis
- vertex
- face
- plane
- sketch point

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md)  
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.md)  
[ISimpleHoleFeatureData2::SetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~SetDirectionReference.md)  
[ISimpleHoleFeatureData2::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ReverseDirection.md)
