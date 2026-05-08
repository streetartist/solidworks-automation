# Loops Property (IChamferFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Loops`

Gets and sets the loops to which a chamfer is applied.
Gets and sets the loops to which a chamfer is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Loops As System.Object
```

```

Dim instance As IChamferFeatureData2
Dim value As System.Object
 
instance.Loops = value
 
value = instance.Loops
```

```

System.object Loops {get; set;}
```

```

property System.Object^ Loops {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of chamfered [loops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Get Chamfer Distances (C#)](Get_Chamfer_Distances_Example_CSharp.htm)  
[Get Chamfer Distances (VB.NET)](Get_Chamfer_Distances_Example_VBNET.htm)  
[Get Chamfer Distances (VBA)](Get_Chamfer_Distances_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)  
[IChamferFeatureData2::IGetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetLoops.md)  
[IChamferFeatureData2::ISetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetLoops.md)  
[IChamferFeatureData2::LoopCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~LoopCount.md)
