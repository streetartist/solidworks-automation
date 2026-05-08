# MaterialID Property (ISimulation3DContactFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~MaterialID`

Gets or sets the type of material the specified component in this 3D Contact feature.
Gets or sets the type of material the specified component in this 3D Contact feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaterialID( _
   ByVal WhichOne As System.Integer _
) As System.Integer
```

```

Dim instance As ISimulation3DContactFeatureData
Dim WhichOne As System.Integer
Dim value As System.Integer
 
instance.MaterialID(WhichOne) = value
 
value = instance.MaterialID(WhichOne)
```

```

System.int MaterialID( 
   System.int WhichOne
) {get; set;}
```

```

property System.int MaterialID {
   System.int get(System.int WhichOne);
   void set (System.int WhichOne, System.int value);
}
```

#### Parameters

*WhichOne*
:   0-based index of the contact component

#### Property Value

Material as defined by [swCosmosWorksMat](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmosWorksMat.html)

Remarks

Available only when [ISimulation3DContactFeatureData::SpecifyMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~SpecifyMaterial.md) is true.

Example

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md)  
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.md)
