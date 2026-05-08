# SetDetachSegmentOnDrag Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~SetDetachSegmentOnDrag`

Sets the Detach Segment on Drag setting.
Sets the Detach Segment on Drag setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDetachSegmentOnDrag( _
   ByVal Detach As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketch
Dim Detach As System.Boolean
Dim value As System.Boolean
 
value = instance.SetDetachSegmentOnDrag(Detach)
```

```

System.bool SetDetachSegmentOnDrag( 
   System.bool Detach
)
```

```

System.bool SetDetachSegmentOnDrag( 
   System.bool Detach
) 
```

#### Parameters

*Detach*
:   True to select Detach Segment on Drag, false to not

#### Return Value

True if Detach Segment on Drag is set, false if not

Remarks

Although this setting can be returned or set at any time, SOLIDWORKS sets it to false upon exiting or entering a sketch. Thus, this method is only useful if called while a sketch is active.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetDetachSegmentOnDrag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetDetachSegmentOnDrag.md)
