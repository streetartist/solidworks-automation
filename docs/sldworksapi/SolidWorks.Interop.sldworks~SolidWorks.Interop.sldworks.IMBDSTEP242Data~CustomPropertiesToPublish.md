# CustomPropertiesToPublish Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data~CustomPropertiesToPublish`

Gets or sets the model's custom properties to export to the STEP 242 format.
Gets or sets the model's custom properties to export to the STEP 242 format.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CustomPropertiesToPublish As System.Object
```

```

Dim instance As IMBDSTEP242Data
Dim value As System.Object
 
instance.CustomPropertiesToPublish = value
 
value = instance.CustomPropertiesToPublish
```

```

System.object CustomPropertiesToPublish {get; set;}
```

```

property System.Object^ CustomPropertiesToPublish {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of custom properties

Remarks

This property is valid only if [IMBDSTEP242Data::PublishWithAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data~PublishWithAllCustomProperties.md) is set to false.

Example

See the [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMBDSTEP242Data Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.md)  
[IMBDSTEP242Data Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data_members.md)
