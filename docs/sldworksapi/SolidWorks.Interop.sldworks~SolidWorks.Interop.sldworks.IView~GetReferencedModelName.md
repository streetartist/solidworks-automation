# GetReferencedModelName Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetReferencedModelName`

Gets the name of the model that is referenced in the drawing view.
Gets the name of the model that is referenced in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReferencedModelName() As System.String
```

```

Dim instance As IView
Dim value As System.String
 
value = instance.GetReferencedModelName()
```

```

System.string GetReferencedModelName()
```

```

System.String^ GetReferencedModelName(); 
```

#### Return Value

Name of the model in the drawing view

Example

[Create Layer for Selected View (VBA)](Create_Layer_for_Selected_View_Example_VB.htm)  
[Get Document Referenced by Drawing View (VBA)](Get_Document_Referenced_by_Drawing_View_Example_VB.htm)  
[Get Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)  
[Traverse Drawing FeatureManager Design Tree (VBA)](Traverse_Drawing_FeatureManager_Design_Tree_Example_VB.htm)  
[Get Configurations Referenced in View (C#)](Get_Configurations_Referenced_in_View_Example_CSharp.htm)  
[Get Configurations Referenced in View (VB.NET)](Get_Configurations_Referenced_in_View_Example_VBNET.htm)  
[Get Configurations Referenced in View (VBA)](Get_Configurations_Referenced_in_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::ReferencedConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfiguration.md)  
[IView::ReferencedDocument Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedDocument.md)  
[IView::ReferencedConfigurationID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfigurationID.md)
