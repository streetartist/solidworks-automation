# LargeDesignReviewMark Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~LargeDesignReviewMark`

Gets or sets whether to add display data to this configuration when the document is saved.
Gets or sets whether to add display data to this configuration when the document is saved.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LargeDesignReviewMark As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
instance.LargeDesignReviewMark = value
 
value = instance.LargeDesignReviewMark
```

```

System.bool LargeDesignReviewMark {get; set;}
```

```

property System.bool LargeDesignReviewMark {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to add display data, false to not

Remarks

This property is valid only if this configuration is one of multiple configurations defined for the assembly or part.

Before SOLIDWORKS 2019, this property specified whether to generate a display list for the configuration of an assembly when it is saved. As of SOLIDWORKS 2019, this property specifies whether to generate a display list for this configuration of:

- an assembly on save. If this property is set to true, the assembly configuration's display list is saved, making the configuration visible in Large Design Review mode. In the user interface, this corresponds to selecting the assembly's **ConfigurationManager >** *configuration\_name* **RMB menu > Add Display Data Mark**.

   - or -

- a part on save. If this property is set to true, the part configuration's display list is saved, making the configuration visible in other applications, such as eDrawings. In the user interface, this corresponds to selecting the part's **ConfigurationManager >** *configuration\_name* **RMB menu > Add Display Data Mark**.

Example

[Get and Set Large Design Review Marks for Configurations (C#)](Get_and_Set_Large_Design_Review_Marks_for_Configurations_Example_CSharp.htm)  
[Get and Set Large Design Review Marks for Configurations (VB.NET)](Get_and_Set_Large_Design_Review_Marks_for_Configurations_Example_VBNET.htm)  
[Get and Set Large Design Review Marks for Configurations (VBA)](Get_and_Set_Large_Design_Review_Marks_for_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IDocumentSpecification::ViewOnly Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ViewOnly.md)
