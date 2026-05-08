# GetPathPointAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetPathPointAtIndex`

Gets the coordinates of a point with the specified index on the path of this revision cloud annotation.
Gets the coordinates of a point with the specified index on the path of this revision cloud annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPathPointAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IRevisionCloud
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetPathPointAtIndex(Index)
```

```

System.object GetPathPointAtIndex( 
   System.int Index
)
```

```

System.Object^ GetPathPointAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of a point on the path of this revision cloud annotation (see **Remarks**)

#### Return Value

Array of doubles of the x, y, and z coordinates of a point on the path of this revision cloud annotation

Remarks

To get the range of values for Index, call [IRevisionCloud::GetPathPointCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetPathPointCount.md) to get the total number of points on the path of this revision cloud annotation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md)  
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.md)  
[IRevisionCloud::IGetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~IGetPathPointAtIndex.md)  
[IRevisionCloud::SetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~SetPathPointAtIndex.md)
