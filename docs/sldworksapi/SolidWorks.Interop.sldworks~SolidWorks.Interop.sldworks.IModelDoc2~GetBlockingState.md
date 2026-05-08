# GetBlockingState Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetBlockingState`

Gets the current value of the SOLIDWORKS blocking state, within the range of values accessible by IModelDoc2::SetBlockingState.
Gets the current value of the SOLIDWORKS blocking state, within the range of values accessible by [IModelDoc2::SetBlockingState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetBlockingState.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBlockingState() As System.Integer
```

```

Dim instance As IModelDoc2
Dim value As System.Integer
 
value = instance.GetBlockingState()
```

```

System.int GetBlockingState()
```

```

System.int GetBlockingState(); 
```

#### Return Value

State as defined by [swBlockingStates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBlockingStates_e.html)

Example

[Get Blocking State (VBA)](Get_Blocking_State_Example_VB.htm)  
[Set Blocking State (VBA)](Set_Blocking_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ResetBlockingState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetBlockingState.md)
