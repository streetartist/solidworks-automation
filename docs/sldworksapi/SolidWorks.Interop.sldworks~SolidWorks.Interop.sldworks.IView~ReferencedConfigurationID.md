# ReferencedConfigurationID Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfigurationID`

Gets the persistent reference ID of the configuration referenced in this drawing view.
Gets the persistent reference ID of the configuration referenced in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferencedConfigurationID As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.ReferencedConfigurationID
```

```

System.int ReferencedConfigurationID {get;}
```

```

property System.int ReferencedConfigurationID {
   System.int get();
}
```

#### Property Value

Referenced configuration's persistent reference ID

Remarks

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

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
[IView::GetReferencedModelName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetReferencedModelName.md)  
[IView::ReferencedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfiguration.md)  
[IView::ReferencedDocument Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedDocument.md)  
[IModelDocExtension::GetObjectByPersistReference3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.md)  
[IModelDocExtension::GetPersistReference3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.md)
