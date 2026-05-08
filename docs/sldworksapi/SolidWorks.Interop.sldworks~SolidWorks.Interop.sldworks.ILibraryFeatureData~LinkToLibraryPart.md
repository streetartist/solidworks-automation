# LinkToLibraryPart Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~LinkToLibraryPart`

Gets or sets whether to the link the library feature to its parent library feature document.
Gets or sets whether to the link the library feature to its parent library feature document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkToLibraryPart As System.Boolean
```

```

Dim instance As ILibraryFeatureData
Dim value As System.Boolean
 
instance.LinkToLibraryPart = value
 
value = instance.LinkToLibraryPart
```

```

System.bool LinkToLibraryPart {get; set;}
```

```

property System.bool LinkToLibraryPart {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to link the library feature to its parent library feature document, false to not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)  
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)  
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::LibraryPart Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~LibraryPart.md)  
[ILibraryFeatureData::Initialize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~Initialize.md)
