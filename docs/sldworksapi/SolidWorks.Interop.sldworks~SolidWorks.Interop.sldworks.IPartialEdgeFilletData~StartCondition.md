# StartCondition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~StartCondition`

Gets the type of start condition for this partial edge fillet.
Gets the type of start condition for this partial edge fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property StartCondition As System.Integer
```

```

Dim instance As IPartialEdgeFilletData
Dim value As System.Integer
 
value = instance.StartCondition
```

```

System.int StartCondition {get;}
```

```

property System.int StartCondition {
   System.int get();
}
```

#### Property Value

Start condition as defined in [swSimpleFilletPartialEdgeCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSimpleFilletPartialEdgeCondition_e.html)

Remarks

To modify the start condition of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md)  
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.md)  
[IPartialEdgeFilletData::EndCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~EndCondition.md)  
[IPartialEdgeFilletData::DistanceOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetStart.md)  
[IPartialEdgeFilletData::PercentOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~PercentOffsetStart.md)  
[IPartialEdgeFilletData::ReferenceOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStart.md)
