# SelectChain Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~SelectChain`

Selects chains of entities attached to this sketch segment.
Selects chains of entities attached to this sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectChain( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

```

Dim instance As ISketchSegment
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean
 
value = instance.SelectChain(Append, Data)
```

```

System.bool SelectChain( 
   System.bool Append,
   SelectData Data
)
```

```

System.bool SelectChain( 
   System.bool Append,
   SelectData^ Data
) 
```

#### Parameters

*Append*
:   True to append to the current selection list, false to replace the selection list

*Data*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md)

#### Return Value

True if successful, false if not

Remarks

Before calling this method call [ISelectionMgr::CreateSelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateSelectData.md) to specify Data.

This method is equivalent to right-clicking a sketch segment and selecting **Select Chain**. The chain of entities in each direction is selected. Selection ends when a branch in the chain is encountered.

Example

[Select Chains of Entities Attached to a Sketch Segment (VBA)](Select_Chain_of_Entities_Example_VB.htm)  
[Select Chains of Entities Attached to a Sketch Segment (VB.NET)](Select_Chain_of_Entities_Example_VBNET.htm)  
[Select Chains of Entities Attached to a Sketch Segment (C#)](Select_Chain_of_Entities_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)
