# GetPreSelectedObject Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetPreSelectedObject`

Gets the preselected object when the preselection notify event is fired.
Gets the preselected object when the preselection notify event is fired.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPreSelectedObject() As System.Object
```

```

Dim instance As ISelectionMgr
Dim value As System.Object
 
value = instance.GetPreSelectedObject()
```

```

System.object GetPreSelectedObject()
```

```

System.Object^ GetPreSelectedObject(); 
```

#### Return Value

Preselected object

Example

[Get Preselected Object (C#)](Get_Preselected_Object_Example_CSharp.htm)  
[Get Preselected Object (VB.NET)](Get_Preselected_Object_Example_VBNET.htm)  
[Get Preselected Object (VBA)](Get_Preselected_Object_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[DAssemblyDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UserSelectionPreNotifyEventHandler.md)  
[DDrawingDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UserSelectionPreNotifyEventHandler.md)  
[DPartDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPreNotifyEventHandler.md)
