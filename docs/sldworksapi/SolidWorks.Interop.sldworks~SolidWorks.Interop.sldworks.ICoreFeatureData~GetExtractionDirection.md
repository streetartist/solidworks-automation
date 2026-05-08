# GetExtractionDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~GetExtractionDirection`

Gets the entities that define the extraction direction of this core feature.
Gets the entities that define the extraction direction of this core feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExtractionDirection( _
   ByRef Type1 As System.Integer, _
   ByRef PDir1 As System.Object, _
   ByRef Type2 As System.Integer, _
   ByRef PDir2 As System.Object _
) As System.Integer
```

```

Dim instance As ICoreFeatureData
Dim Type1 As System.Integer
Dim PDir1 As System.Object
Dim Type2 As System.Integer
Dim PDir2 As System.Object
Dim value As System.Integer
 
value = instance.GetExtractionDirection(Type1, PDir1, Type2, PDir2)
```

```

System.int GetExtractionDirection( 
   out System.int Type1,
   out System.object PDir1,
   out System.int Type2,
   out System.object PDir2
)
```

```

System.int GetExtractionDirection( 
   [Out] System.int Type1,
   [Out] System.Object^ PDir1,
   [Out] System.int Type2,
   [Out] System.Object^ PDir2
) 
```

#### Parameters

*Type1*
:   Type of entity as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

*PDir1*
:   Entity that defines the extraction direction (see **Remarks**)

*Type2*
:   Type of entity as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

*PDir2*
:   Entity that defines the extraction direction (see Remarks)

#### Return Value

Number of entities that define the extraction direction

Remarks

The types of entities that define the extraction direction are:

- Face
- Plane
- Edge
- Vertex
- Sketch line
- Sketch point

There can be two entities because two sketch points can specify a direction.

Example

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)  
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)  
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md)  
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.md)  
[ICoreFeatureData::SetExtractionDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~SetExtractionDirection.md)
