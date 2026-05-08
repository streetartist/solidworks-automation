# EndDirectionVector Property (ILoftFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndDirectionVector`

Gets or sets the direction vector in which to end this loft feature.
Gets or sets the direction vector in which to end this loft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EndDirectionVector As System.Object
```

```

Dim instance As ILoftFeatureData
Dim value As System.Object
 
instance.EndDirectionVector = value
 
value = instance.EndDirectionVector
```

```

System.object EndDirectionVector {get; set;}
```

```

property System.Object^ EndDirectionVector {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

End direction vector

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.md)  
[ILoftFeatureData::StartDirectionVector Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartDirectionVector.md)
