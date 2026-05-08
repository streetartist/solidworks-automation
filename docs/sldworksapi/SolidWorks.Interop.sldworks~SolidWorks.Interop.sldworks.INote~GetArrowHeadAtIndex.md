# GetArrowHeadAtIndex Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadAtIndex`

Gets information on the specified arrowhead in this note.
Gets information on the specified arrowhead in this note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As INote
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetArrowHeadAtIndex(Index)
```

```

System.object GetArrowHeadAtIndex( 
   System.int Index
)
```

```

System.Object^ GetArrowHeadAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired arrowhead where the index begins at 0

#### Return Value

Array of doubles (see **Remarks**)

Remarks

This method returns an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. This information is independent of whether this note actually has an arrowhead.

Format of return information is the following array of doubles:

- return value[0] = arrow length (i.e. leader into arrowhead)
- return value[1] = arrowhead length
- return value[2] = arrowhead width

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArrowHeadAtIndex.md)  
[INote::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArrowHeadInfo.md)  
[INote::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadCount.md)  
[INote::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadInfo.md)
