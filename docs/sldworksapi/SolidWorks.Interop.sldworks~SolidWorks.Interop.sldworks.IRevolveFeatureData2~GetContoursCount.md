# GetContoursCount Method (IRevolveFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetContoursCount`

Gets the number of selected contours for this revolve feature.
Gets the number of selected contours for this revolve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetContoursCount() As System.Integer
```

```

Dim instance As IRevolveFeatureData2
Dim value As System.Integer
 
value = instance.GetContoursCount()
```

```

System.int GetContoursCount()
```

```

System.int GetContoursCount(); 
```

#### Return Value

Number of selected contours

Remarks

This method returns the total number of sketch contours and sketch regions used in the base sketch for this feature.

Call this method before calling [IRevolveFeatureData2::IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetContours.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)  
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.md)  
[IRevolveFeatureData2::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ISetContours.md)  
[IRevolveFeatureData2::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Contours.md)
