# LinkParentConfiguration Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~LinkParentConfiguration`

Gets or sets whether to link a projected or auxiliary view with the parent configuration.
Gets or sets whether to link a projected or auxiliary view with the parent configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkParentConfiguration As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
instance.LinkParentConfiguration = value
 
value = instance.LinkParentConfiguration
```

```

System.bool LinkParentConfiguration {get; set;}
```

```

property System.bool LinkParentConfiguration {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to link a projected or auxiliary view with the parent configuration, false to not

Remarks

After setting this property, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md).

Example

[Link Projected View to Parent Configuration (C#)](Link_Projected_View_to_Parent_Configuration_Example_CSharp.htm)  
[Link Projected View to Parent Configuration (VB.NET)](Link_Projected_View_to_Parent_Configuration_Example_VBNET.htm)  
[Link Projected View to Parent Configuration (VBA)](Link_Projected_View_to_Parent_Configuration_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
