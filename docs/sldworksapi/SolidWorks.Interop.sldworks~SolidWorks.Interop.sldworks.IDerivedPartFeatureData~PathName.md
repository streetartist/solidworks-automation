# PathName Property (IDerivedPartFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~PathName`

Gets the path for the derived part feature.
Gets the path for the derived part feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PathName As System.String
```

```

Dim instance As IDerivedPartFeatureData
Dim value As System.String
 
instance.PathName = value
 
value = instance.PathName
```

```

System.string PathName {get; set;}
```

```

property System.String^ PathName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Fully qualified path and file name of the derived part feature

Example

[Modify Derived Part (C#)](Modify_Derived_Part_Example_CSharp.htm)  
[Modify Derived Part (VB.NET)](Modify_Derived_Part_Example_VBNET.htm)  
[Modify Derived Part (VBA)](Modify_Derived_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)  
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.md)
