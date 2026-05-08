# IGetID Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetID`

Gets the ID for this sketch segment.
Gets the ID for this sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetID() As System.Integer
```

```

Dim instance As ISketchSegment
Dim value As System.Integer
 
value = instance.IGetID()
```

```

System.int IGetID()
```

```

System.int IGetID(); 
```

#### Return Value

Array with two longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) identifying this sketch segment ID

Remarks

The ID of the sketch segment:

- is an ordered pair (i1, i2). For the specific sketch segment type, for example, line, arc, spline, and so on), the combination of these two numbers is always unique within a specific sketch.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm).

Each entity within a specific sketch has a unique ID. However, a sketch line may have the same ID values as a sketch arc within the same sketch. Likewise, in a second sketch, you may find a different sketch element with the same ID Therefore, your application must keep track of:

- sketch element type (that is, point, line, arc, spline, and so on)
- owning sketch name
- sketch element id to uniquely identify a sketched item

You can determine the sketch element type by using [ISketchSegment::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetType.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::GetID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetID.md)
