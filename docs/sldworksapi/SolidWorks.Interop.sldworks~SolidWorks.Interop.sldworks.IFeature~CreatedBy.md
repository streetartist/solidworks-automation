# CreatedBy Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CreatedBy`

Gets the name of the user who created the feature.
Gets the name of the user who created the feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CreatedBy As System.String
```

```

Dim instance As IFeature
Dim value As System.String
 
value = instance.CreatedBy
```

```

System.string CreatedBy {get;}
```

```

property System.String^ CreatedBy {
   System.String^ get();
}
```

#### Property Value

Name of the user who created the feature

Example

[Get Names of Creators of Features (VBA)](Get_Names_of_Creators_of_Features_Example_VB.htm)  
[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)  
[Get Names of Creators of Features (C#)](Get_Names_of_Creators_of_Features_Example_CSharp.htm)  
[Get Names of Creators of Features (VB.NET)](Get_Names_of_Creators_of_Features_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::DateCreated Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateCreated.md)  
[IFeature::DateModified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateModified.md)
