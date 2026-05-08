# ReferencedConfiguration Property (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfiguration`

Gets or sets the configuration referenced by this drawing view.
Gets or sets the configuration referenced by this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferencedConfiguration As System.String
```

```

Dim instance As IView
Dim value As System.String
 
instance.ReferencedConfiguration = value
 
value = instance.ReferencedConfiguration
```

```

System.string ReferencedConfiguration {get; set;}
```

```

property System.String^ ReferencedConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the configuration for the drawing view

Remarks

After changing the configuration, you must call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) to see the changes.

Example

[Get Configurations Referenced in View (C#)](Get_Configurations_Referenced_in_View_Example_CSharp.htm)  
[Get Configurations Referenced in View (VB.NET)](Get_Configurations_Referenced_in_View_Example_VBNET.htm)  
[Get Configurations Referenced in View (VBA)](Get_Configurations_Referenced_in_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetReferencedModelName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetReferencedModelName.md)  
[IView::ReferencedDocument Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedDocument.md)  
[IView::ReferencedConfigurationID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfigurationID.md)
