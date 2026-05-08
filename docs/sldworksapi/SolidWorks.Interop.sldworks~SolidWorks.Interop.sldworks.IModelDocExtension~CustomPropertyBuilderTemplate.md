# CustomPropertyBuilderTemplate Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyBuilderTemplate`

Gets or sets the custom property builder template for this part.
Gets or sets the custom property builder template for this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CustomPropertyBuilderTemplate( _
   ByVal WeldmentTemplate As System.Boolean _
) As System.String
```

```

Dim instance As IModelDocExtension
Dim WeldmentTemplate As System.Boolean
Dim value As System.String
 
instance.CustomPropertyBuilderTemplate(WeldmentTemplate) = value
 
value = instance.CustomPropertyBuilderTemplate(WeldmentTemplate)
```

```

System.string CustomPropertyBuilderTemplate( 
   System.bool WeldmentTemplate
) {get; set;}
```

```

property System.String^ CustomPropertyBuilderTemplate {
   System.String^ get(System.bool WeldmentTemplate);
   void set (System.bool WeldmentTemplate, System.String^ value);
}
```

#### Parameters

*WeldmentTemplate*
:   True if a weldment part, false if not (see **Remarks**)

#### Property Value

File name of the custom property builder template (see **Remarks**)

Remarks

If WeldmentTemplate is:

- True, then this property gets or sets **\*.wldprp**.
- False, then this property gets or sets **\*.prtprp**.

All custom property builder templates are stored in the file location specified in **Tools > Options > File Locations > Custom Property Files**.

This property corresponds to the setting in the Template Options dialog that appears when you click on the button next to More Properties in the Custom Properties task pane. When you create a custom property layout, a template is created. The button is activated for parts and weldments only after a custom properties tab layout is created. The weldment custom property template (**\*.wldprp**) can be created or modified only if a cut list item is selected in the Cut list folder.

Example

```

swModDocExt.CustomPropertyBuilderTemplate(False) = "template.prtprp"
```

```

swModDocExt.CustomPropertyBuilderTemplate(True) = "templateWeld2.wldprp"
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
