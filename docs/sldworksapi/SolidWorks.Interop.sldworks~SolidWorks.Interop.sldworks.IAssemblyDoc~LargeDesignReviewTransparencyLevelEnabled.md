# LargeDesignReviewTransparencyLevelEnabled Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelEnabled`

Gets or sets whether transparency levels are activated for unmodified components in the graphics area for this assembly opened in Large Design Review mode.
Gets or sets whether transparency levels are activated for unmodified components in the graphics area for this assembly opened in Large Design Review mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LargeDesignReviewTransparencyLevelEnabled As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim value As System.Boolean
 
instance.LargeDesignReviewTransparencyLevelEnabled = value
 
value = instance.LargeDesignReviewTransparencyLevelEnabled
```

```

System.bool LargeDesignReviewTransparencyLevelEnabled {get; set;}
```

```

property System.bool LargeDesignReviewTransparencyLevelEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if transparency levels are activated, false if not

Remarks

This property is valid only when the assembly is opened in Large Design Review mode, and one or more of its components have been modified. If this property is enabled, modified components are opaque, and unmodified components are transparent.

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
[IAssemblyDoc::LargeDesignReviewTransparencyLevelDynamic Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelDynamic.md)
