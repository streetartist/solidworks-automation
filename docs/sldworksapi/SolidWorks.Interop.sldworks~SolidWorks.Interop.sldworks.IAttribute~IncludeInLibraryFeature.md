# IncludeInLibraryFeature Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IncludeInLibraryFeature`

Gets or sets whether this attribute is included in the library feature.
Gets or sets whether this attribute is included in the library feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeInLibraryFeature As System.Boolean
```

```

Dim instance As IAttribute
Dim value As System.Boolean
 
instance.IncludeInLibraryFeature = value
 
value = instance.IncludeInLibraryFeature
```

```

System.bool IncludeInLibraryFeature {get; set;}
```

```

property System.bool IncludeInLibraryFeature {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the attribute is included in the library feature, false if not

Remarks

Attributes included in a library feature are propagated to each instance of that library feature. However, If an entity (e.g., face, edge, etc.) is shared among features and all of these features are not included in the library feature, then the attribute is not propagated.

Example

[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)  
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)  
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md)  
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.md)  
[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)
