# InteractiveComponentSelection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveComponentSelection`

Gets whether to display the Selective Open dialog, which allows the interactive user to either select and open specific components or open all of the displayed components.
Gets whether to display the Selective Open dialog, which allows the interactive user to either select and open specific components or open all of the displayed components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InteractiveComponentSelection As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.InteractiveComponentSelection = value
 
value = instance.InteractiveComponentSelection
```

```

System.bool InteractiveComponentSelection {get; set;}
```

```

property System.bool InteractiveComponentSelection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display the Selective Open dialog to the interactive user, false to not (default)

Remarks

This property is not valid for opening **3D**EXPERIENCE files using SOLIDWORKS Connected.

If this property is set to true, than any components added to the components list by [IDocumentSpecification::ComponentList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ComponentList.md) are ignored.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)  
[IDocumentSpecification::Selective Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Selective.md)
