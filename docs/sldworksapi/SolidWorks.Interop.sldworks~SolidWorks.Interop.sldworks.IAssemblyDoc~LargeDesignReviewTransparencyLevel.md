# LargeDesignReviewTransparencyLevel Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevel`

Gets or sets the transparency level of unmodified components in the graphics area of this assembly opened in Large Design Review mode.
Gets or sets the transparency level of unmodified components in the graphics area of this assembly opened in Large Design Review mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LargeDesignReviewTransparencyLevel As System.Double
```

```

Dim instance As IAssemblyDoc
Dim value As System.Double
 
instance.LargeDesignReviewTransparencyLevel = value
 
value = instance.LargeDesignReviewTransparencyLevel
```

```

System.double LargeDesignReviewTransparencyLevel {get; set;}
```

```

property System.double LargeDesignReviewTransparencyLevel {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 (opaque) <= transparency level of unmodified components <= 1.0 (invisible)

Remarks

This property is valid only if all of the following are true:

- This assembly is opened in Large Design Review mode.
- One or more assembly components have been modified.
- [IAssemblyDoc::LargeDesignReviewTransparencyLevelEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelEnabled.md) is set to true.

When transparency levels are enabled, modified components are opaque, and unmodified components have the transparency level specified by this property.

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
[IAssemblyDoc::LargeDesignReviewTransparencyLevelDynamic Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelDynamic.md)
