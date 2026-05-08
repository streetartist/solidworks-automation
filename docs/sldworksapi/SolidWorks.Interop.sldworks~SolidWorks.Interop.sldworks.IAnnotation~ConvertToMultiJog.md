# ConvertToMultiJog Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ConvertToMultiJog`

Converts a note with a leader to a note with a multi-jog leader.
Converts a note with a leader to a note with a multi-jog leader.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ConvertToMultiJog( _
   ByVal LeaderNumber As System.Integer, _
   ByVal NumberOfPoints As System.Integer, _
   ByVal PointsData As System.Object _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim LeaderNumber As System.Integer
Dim NumberOfPoints As System.Integer
Dim PointsData As System.Object
Dim value As System.Boolean
 
value = instance.ConvertToMultiJog(LeaderNumber, NumberOfPoints, PointsData)
```

```

System.bool ConvertToMultiJog( 
   System.int LeaderNumber,
   System.int NumberOfPoints,
   System.object PointsData
)
```

```

System.bool ConvertToMultiJog( 
   System.int LeaderNumber,
   System.int NumberOfPoints,
   System.Object^ PointsData
) 
```

#### Parameters

*LeaderNumber*
:   :   Number of the leader to convert in the 0-based list of leaders

*NumberOfPoints*
:   Number of jog points

*PointsData*
:   :   Array of doubles, whose size is 3\*NumberOfPoints, that specify the points where to locate the jogs; the points are in sheet space

#### Return Value

True if the leader is converted to a multi-jog leader, false if not

Example

**Visual Basic for Applications (VBA)**

 

' Convert the first leader of the note to a two-point multi-jog leader

...

Dim vPointData as Variant

Dim nPoints (0 to 6) as Double

nPoints(0) = 0.189013

nPoints(1) = 0.248742

nPoints(2) = -1.75647E-15

nPoints(3) = 0.252176

nPoints(4) = 0.186859

nPoints(5) = -1.32434E-15

...

vPointData = nPoints

boolstatus = Annotation.ConvertToMultiJog(0, 2, (vPointData))

...

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
