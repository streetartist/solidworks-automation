# SetDirectionReference Method (ISimpleHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~SetDirectionReference`

Sets the direction of the cut extrude for this simple hole feature.
Sets the direction of the cut extrude for this simple hole feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDirectionReference( _
   ByVal Ref1 As System.Object, _
   ByVal Ref2 As System.Object _
) As System.Boolean
```

```

Dim instance As ISimpleHoleFeatureData2
Dim Ref1 As System.Object
Dim Ref2 As System.Object
Dim value As System.Boolean
 
value = instance.SetDirectionReference(Ref1, Ref2)
```

```

System.bool SetDirectionReference( 
   System.object Ref1,
   System.object Ref2
)
```

```

System.bool SetDirectionReference( 
   System.Object^ Ref1,
   System.Object^ Ref2
) 
```

#### Parameters

*Ref1*
:   First reference entity (see **Remarks**)

*Ref2*
:   Second reference entity (see **Remarks**)

#### Return Value

True if the direction for the cut is set, false if not

Remarks

Sometimes one reference entity defines a direction; for example, an edge or axis. Other times, two reference entities define a direction; for example, two vertices or two sketch points.

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
[ISimpleHoleFeatureData2::GetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetDirectionReference.md)  
[ISimpleHoleFeatureData2::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ReverseDirection.md)
