# ResetBlockingState Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetBlockingState`

Resets the blocking state for the SOLIDWORKS menus.
Resets the blocking state for the SOLIDWORKS menus.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ResetBlockingState() 
```

```

Dim instance As IModelDoc2
 
instance.ResetBlockingState()
```

```

void ResetBlockingState()
```

```

void ResetBlockingState(); 
```

Remarks

Call this method after calling [IModelDoc2::SetBlockingState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetBlockingState.md) to set the SOLIDWORKS menus back to their previous state.

NOTE: You must call this method every time you call IModelDoc2::SetBlockingState. It is not enough to call this method once at the end of a sequence of operations that have called IModelDoc2::SetBlockingState several times.

Example

[Set Blocking State (VBA)](Set_Blocking_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
