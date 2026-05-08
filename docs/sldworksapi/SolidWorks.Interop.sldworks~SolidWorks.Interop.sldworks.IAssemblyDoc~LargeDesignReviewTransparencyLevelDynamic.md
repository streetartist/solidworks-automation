# LargeDesignReviewTransparencyLevelDynamic Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelDynamic`

Gets or sets whether to dynamically modify the transparency level of unmodified components in the graphics area when the transparency level slider is moved on the Filter Modified Components PropertyManager page.
Gets or sets whether to dynamically modify the transparency level of unmodified components in the graphics area when the transparency level slider is moved on the Filter Modified Components PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LargeDesignReviewTransparencyLevelDynamic As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim value As System.Boolean
 
instance.LargeDesignReviewTransparencyLevelDynamic = value
 
value = instance.LargeDesignReviewTransparencyLevelDynamic
```

```

System.bool LargeDesignReviewTransparencyLevelDynamic {get; set;}
```

```

property System.bool LargeDesignReviewTransparencyLevelDynamic {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to dynamically modify the transparency level of unmodified components in the graphics area when moving the transparency level slider, false to not

Remarks

This property is valid only when the assembly is opened in Large Design Review mode, and one or more of its components have been modified. When this property is enabled, modified components are opaque, and unmodified components change transparency as the transparency level slider moves.

The Filter Modified Components PropertyManager page appears when you click **Filter Modified Components** on the Large Design Review toolbar.

Example

[Set Transparency of Components in Large Design Review (C#)](Set_Transparency_of_Components_LDR_Mode_Example_CSharp.htm)  
[Set Transparency of Components in Large Design Review (VB.NET)](Set_Transparency_of_Components_LDR_Mode_Example_VBNET.htm)  
[Set Transparency of Components in Large Design Review (VBA)](Set_Transparency_of_Components_LDR_Mode_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::LargeDesignReviewTransparencyLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevel.md)  
[IAssemblyDoc::LargeDesignReviewTransparencyLevelEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelEnabled.md)
