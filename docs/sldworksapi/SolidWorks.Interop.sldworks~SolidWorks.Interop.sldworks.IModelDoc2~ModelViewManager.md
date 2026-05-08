# ModelViewManager Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ModelViewManager`

Gets the IModelViewManager object, which allows access to the model view.
Gets the [IModelViewManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md) object, which allows access to the model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ModelViewManager As ModelViewManager
```

```

Dim instance As IModelDoc2
Dim value As ModelViewManager
 
value = instance.ModelViewManager
```

```

ModelViewManager ModelViewManager {get;}
```

```

property ModelViewManager^ ModelViewManager {
   ModelViewManager^ get();
}
```

Example

[Create Drag Arrow Manipulator (VBA)](Create_Drag_Arrow_Manipulator_Example_VB.htm)  
[Set Viewports (C#)](Set_Viewports_Example_CSharp.htm)  
[Set Viewports (VB.NET)](Set_Viewports_Example_VBNET.htm)  
[Set Viewports (VBA)](Set_Viewports_Example_VB.htm)  
[Add ActiveX Tabs to Model View (C#)](Add_ActiveX_Tabs_to_Model_View_Example_CSharp.htm)  
[Add ActiveX Tabs to Model View (VB.NET)](Add_ActiveX_Tabs_to_Model_View_Example_VBNET.htm)  
[Add ActiveX Tabs to Model View (VBA)](Add_ActiveX_Tabs_to_Model_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
