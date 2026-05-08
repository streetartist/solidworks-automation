# GetID Method (ISketchHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~GetID`

Gets the ID for this sketch hatch.
Gets the ID for this sketch hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetID() As System.Object
```

```

Dim instance As ISketchHatch
Dim value As System.Object
 
value = instance.GetID()
```

```

System.object GetID()
```

```

System.Object^ GetID(); 
```

#### Return Value

Array with two longs or two integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) identifying this sketch hatch ID (see **Remarks**)

Remarks

The ID of the sketch hatch:

- is an ordered pair (i1, i2). The combination of these two numbers is always unique within a specific sketch.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm).

Each entity within a specific sketch has a unique ID. However, a sketch line can have the same ID values as a sketch arc within the same sketch. Likewise, in a second sketch, you may find a different sketch element with the same ID. Therefore, your application must keep track of:

- sketch element type (that is, point, line, arc, spline, and so on)
- owning sketch name
- sketch element ID to uniquely identify a sketched item

You can determine the sketch element type by using [ISketchSegment::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetType.md).

Example

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)  
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.md)  
[ISketchHatch::IGetID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetID.md)
