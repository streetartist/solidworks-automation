# SetPathPointAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~SetPathPointAtIndex`

Sets the specified coordinates of a point at the specified index on the path of this revision cloud annotation.
Sets the specified coordinates of a point at the specified index on the path of this revision cloud annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPathPointAtIndex( _
   ByVal Index As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

```

Dim instance As IRevisionCloud
Dim Index As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.SetPathPointAtIndex(Index, X, Y, Z)
```

```

System.bool SetPathPointAtIndex( 
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.bool SetPathPointAtIndex( 
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*Index*
:   Index of an existing point on the path of this revision cloud annotation; -1 if creating a new point (see **Remarks**)

*X*
:   x coordinate of the point

*Y*
:   y coordinate of the point

*Z*
:   z coordinate of the point

#### Return Value

True if successful, false if not

Remarks

To get the range of values for Index, call [IRevisionCloud::GetPathPointCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetPathPointCount.md) to get the total number of points on the path of this revision cloud annotation.

You can create a new path point by calling this method, setting Index to -1. You can create new path points any time after [IDrawingDoc::InsertRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionCloud.md) or [IDrawingDoc::IInsertRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertRevisionCloud.md) is called. You cannot create new path points after [IRevisionCloud::Finalize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~Finalize.md) is called.

You can call this method at any time to change the position of existing path points.

Example

See [IRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md)  
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.md)  
[IRevisionCloud::GetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetPathPointAtIndex.md)  
[IRevisionCloud::IGetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~IGetPathPointAtIndex.md)
