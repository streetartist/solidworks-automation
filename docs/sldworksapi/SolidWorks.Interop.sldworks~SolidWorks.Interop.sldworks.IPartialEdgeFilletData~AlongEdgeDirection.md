# AlongEdgeDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~AlongEdgeDirection`

Gets which end of the edge to start the fillet.
Gets which end of the edge to start the fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property AlongEdgeDirection As System.Boolean
```

```

Dim instance As IPartialEdgeFilletData
Dim value As System.Boolean
 
value = instance.AlongEdgeDirection
```

```

System.bool AlongEdgeDirection {get;}
```

```

property System.bool AlongEdgeDirection {
   System.bool get();
}
```

#### Property Value

True to start the fillet at the start point of the edge, false to start the fillet at the end point of the edge

Remarks

To modify the starting point of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md)  
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.md)
