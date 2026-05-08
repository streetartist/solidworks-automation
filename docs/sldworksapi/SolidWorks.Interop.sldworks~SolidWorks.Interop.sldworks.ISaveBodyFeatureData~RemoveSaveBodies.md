# RemoveSaveBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~RemoveSaveBodies`

Removes the specified bodies from this Save Bodies feature.
Removes the specified bodies from this Save Bodies feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveSaveBodies( _
   ByVal Bodies As System.Object _
) As System.Boolean
```

```

Dim instance As ISaveBodyFeatureData
Dim Bodies As System.Object
Dim value As System.Boolean
 
value = instance.RemoveSaveBodies(Bodies)
```

```

System.bool RemoveSaveBodies( 
   System.object Bodies
)
```

```

System.bool RemoveSaveBodies( 
   System.Object^ Bodies
) 
```

#### Parameters

*Bodies*
:   Array of bodies to remove from this Save Bodies feature

#### Return Value

True if the bodies are removed from this Save Bodies feature, false if not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.md)  
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.md)  
[ISaveBodyFeatureData::AddSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~AddSaveBodies.md)  
[ISaveBodyFeatureData::GetSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~GetSaveBodies.md)
