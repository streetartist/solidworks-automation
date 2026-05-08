# Edge Property (ICosmeticThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~Edge`

Gets or sets the circular edge to which this cosmetic thread is attached.
Gets or sets the circular edge to which this cosmetic thread is attached.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Edge As Edge
```

```

Dim instance As ICosmeticThreadFeatureData
Dim value As Edge
 
instance.Edge = value
 
value = instance.Edge
```

```

Edge Edge {get; set;}
```

```

property Edge^ Edge {
   Edge^ get();
   void set (    Edge^ value);
}
```

#### Property Value

Circular [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) to which this cosmetic thread is attached

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Get Cosmetic Threads Features in a Part (VBA)](Get_Cosmetic_Threads_in_a_Part_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md)  
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.md)
