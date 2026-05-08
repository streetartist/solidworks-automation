# GetLeaderNumPointsAt Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderNumPointsAt`

Gets the number of points in the specified leader of this note.
Gets the number of points in the specified leader of this note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLeaderNumPointsAt( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As INote
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetLeaderNumPointsAt(Index)
```

```

System.int GetLeaderNumPointsAt( 
   System.int Index
)
```

```

System.int GetLeaderNumPointsAt( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of leader on this note

#### Return Value

Number of points in the leader

Remarks

Use [INote::GetLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderCount.md) to see how many leaders are on the note.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetLeaderAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderAtIndex.md)  
[INote::GetLeaderInfo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderInfo.md)  
[INote::SetZeroLengthLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.md)  
[INote::HasExtraLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasExtraLeader.md)  
[INote::IsAttached Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsAttached.md)
