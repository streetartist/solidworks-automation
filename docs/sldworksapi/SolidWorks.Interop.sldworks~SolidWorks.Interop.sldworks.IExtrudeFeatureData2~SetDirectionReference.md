# SetDirectionReference Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDirectionReference`

Sets the direction of the extrusion.
Sets the direction of the extrusion.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDirectionReference( _
   ByVal Ref1 As System.Object, _
   ByVal Ref2 As System.Object _
) 
```

```

Dim instance As IExtrudeFeatureData2
Dim Ref1 As System.Object
Dim Ref2 As System.Object
 
instance.SetDirectionReference(Ref1, Ref2)
```

```

void SetDirectionReference( 
   System.object Ref1,
   System.object Ref2
)
```

```

void SetDirectionReference( 
   System.Object^ Ref1,
   System.Object^ Ref2
) 
```

#### Parameters

*Ref1*
:   First reference entity

*Ref2*
:   Second reference entity

Remarks

Sometimes one reference entity can sufficiently define a direction; for example, an edge or axis. Other times, two reference entities are required to define a direction; for example, two vertices or two sketch points.

|  |  |
| --- | --- |
| **If...** | **Then...** |
| One reference entity can sufficiently define the direction | Ref2 is NULL |
| Two reference entities are required to define the direction | Both Ref1 and Ref2 are non-NULL |

Valid reference entities for Type1 and Type2:

- line segment
- edge
- axis
- vertex
- face
- plane
- sketch point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::GetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDirectionReference.md)  
[IExtrudeFeatureData2::GetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDirectionReference.md)
